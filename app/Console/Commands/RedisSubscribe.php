<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use Illuminate\Support\Facades\Redis;
use App\Repositories\EventRepository;

class RedisSubscribe extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'redis:subscribe';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Subscribe to a Redis channel';

    /**
     * Execute the console command.
     *
     * @return mixed
     */
    public function handle()
    {
        Redis::psubscribe(['schedule.*'], function ($message, $channel) {
            $event = new EventRepository();
            switch($channel) {
                case 'schedule.session.create':
                    $decoded = json_decode($message, true);
                    $fetchedEvent = $event->get($decoded['eventId']);
                    $event->create([
                        'room' => $decoded['room'],
                        'startDate' => $decoded['startDate'],
                        'endDate' => $decoded['endDate'],
                        'startTime' => $decoded['startTime'],
                        'endTime' => $decoded['endTime'],
                        'eventTypeId' => $decoded['eventTypeId'],
                        'groupId' => $fetchedEvent['groupId'],
                        'subjectId' => $fetchedEvent['subjectId'],
                        'userId' => $fetchedEvent['userId'],
                        'interval' => 1,
                        'frequency' => 'DAILY',
                        'sessionId' => $decoded['sessionId']
                    ]);
                    break;
                case 'schedule.session.delete':
                    $decoded = json_decode($message, true);
                    $fetchedEvent = $event->find(['sessionId' => $decoded['sessionId']]);
                    $event->delete($fetchedEvent['id']);
                    break;
            }
        });
    }
}
