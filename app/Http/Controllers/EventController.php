<?php
namespace App\Http\Controllers;

use App\Repositories\EventRepository;
use App\Repositories\HolidayRepository;
use Carbon\Carbon;
use Illuminate\Http\Request;
use Illuminate\Support\Str;
use RRule\RRule;
use RRule\RSet;

class EventController extends Controller
{

    protected $event;
    protected $holiday;

    public function __construct(EventRepository $event, HolidayRepository $holiday)
    {
        $this->event = $event;
        $this->holiday = $holiday;
    }

    public function store(Request $request)
    {
        $this->validate($request, [
            'room' => 'required',
            'interval' => 'required|integer',
            'frequency' => 'required',
            'startDate' => 'required|date',
            'endDate' => 'required|date',
            'startTime' => 'required',
            'endTime' => 'required',
            'subjectId' => 'required',
            'groupId' => 'required',
            'userId' => 'required',
            'eventTypeId' => 'required',
        ]);

        return $this->event->create($request->all());
    }

    public function show($id)
    {
        return $this->event->get($id);
    }

    public function update(Request $request, $id)
    {
        $this->validate($request, [
            'room' => 'required',
            'interval' => 'required|integer',
            'frequency' => 'required',
            'startDate' => 'required|date',
            'endDate' => 'required|date',
            'startTime' => 'required',
            'endTime' => 'required',
            'subjectId' => 'required',
            'groupId' => 'required',
            'userId' => 'required',
            'eventTypeId' => 'required',
        ]);

        $this->event->update($request->all(), $id);
        return $this->event->get($id);
    }

    public function delete($id)
    {
        $this->event->delete($id);
        return response(null, 204);
    }

    public function index(Request $request)
    {
        $eventList = $this->event->all($request->query());
        if (is_null($request->query('startDate')) && is_null($request->query('endDate'))) {
            return $eventList;
        }
        $holidayRset = new RSet();
        $holidays = $this->holiday->all(null);
        $holidays->each(function ($holiday) use ($holidayRset) {
            $holidayRule = new RRule([
                'FREQ' => 'DAILY',
                'DTSTART' => $holiday['startDate'],
                'UNTIL' => $holiday['endDate'],
                'INTERVAL' => 1,
            ]);
            $holidayRset->addExRule($holidayRule);
        });
        $response = $eventList->map(function ($event) use ($holidayRset, $request) {
            $rset = clone $holidayRset;
            $rules = new RRule([
                'FREQ' => $event['frequency'],
                'DTSTART' => $event['startDate'],
                'UNTIL' => $event['endDate'],
                'INTERVAL' => $event['interval'],
            ]);
            $rset->addRRule($rules);
            $eventArray = [];
            foreach ($rset as $occurence) {
                $date = Carbon::parse($occurence);
                if (Carbon::parse($occurence)->between(Carbon::parse($request->query('startDate')), Carbon::parse($request->query('endDate')))) {
                    array_push($eventArray, [
                        'id' => (string) Str::uuid(),
                        'date' => $date->toDateString(),
                        'frequency' => $event['frequency'],
                        'startTime' => $event['startTime'],
                        'endTime' => $event['endTime'],
                        'room' => $event['room'],
                        'eventId' => $event['id'],
                        'subjectId' => $event['subjectId'],
                        'groupId' => $event['groupId'],
                        'userId' => $event['userId'],
                        'eventTypeId' => $event['eventTypeId'],
                    ]);

                }

            };
            return $eventArray;
        });

        return count($response) ? array_merge(...$response) : [];
    }

}
