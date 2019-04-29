<?php
namespace App\Http\Controllers;

use App\Repositories\EventRepository;
use Illuminate\Http\Request;
use RRule\RRule;

class EventController extends Controller
{

    protected $event;

    public function __construct(EventRepository $event)
    {
        $this->event = $event;
    }

    public function store(Request $request)
    {
        return $this->event->create($request->all());
    }

    public function show($id)
    {
        return $this->event->get($id);
    }

    public function update(Request $request, $id)
    {
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
        $response = [];
        $eventList = $this->event->all($request->query());
        foreach ($eventList as $event) {
            foreach (new RRule([
                'FREQ' => $event['frequency'],
                'DTSTART' => $event['startDate'],
                'UNTIL' => $event['endDate'],
                'INTERVAL' => $event['interval'],
            ]) as $occurence) {
                if ($occurence >= $request->query('startDate') && $occurence <= $request->query('endDate')) {
                    array_push($response, [
                        'date' => $occurence,
                        'startTime' => $event['startTime'],
                        'endTime' => $event['endTime'],
                        'room' => $event['room'],
                        'isFullDay' => $event['isFullDay'],
                        'isNotifiable' => $event['isNotifiable'],
                        'subject' => $event['subject'],
                        'group' => $event['group'],
                        'professorId' => $event['professorId'],
                        'eventType' => $event['eventType'],
                    ]);
                }
            }
        }

        return $response;
    }

}
