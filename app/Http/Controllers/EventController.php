<?php
namespace App\Http\Controllers;

use App\Repositories\EventRepository;
use Carbon\Carbon;
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
        $this->validate($request, [
            'room' => 'required',
            'interval' => 'required|integer',
            'frequency' => 'required',
            'startDate' => 'required|date',
            'endDate' => 'required|date',
            'startTime' => 'required',
            'endTime' => 'required',
            'isFullDay' => 'required|boolean',
            'isNotifiable' => 'required|boolean',
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
            'isFullDay' => 'required|boolean',
            'isNotifiable' => 'required|boolean',
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
        $response = $eventList->map(function ($event) {
            $rules = new RRule([
                'FREQ' => $event['frequency'],
                'DTSTART' => $event['startDate'],
                'UNTIL' => $event['endDate'],
                'INTERVAL' => $event['interval'],
            ]);
            foreach ($rules as $occurence) {
                return [
                    'id' => $event['id'],
                    'date' => Carbon::parse($occurence)->toDateString(),
                    'startTime' => $event['startTime'],
                    'endTime' => $event['endTime'],
                    'room' => $event['room'],
                    'isFullDay' => filter_var($event['isFullDay'], FILTER_VALIDATE_BOOLEAN),
                    'isNotifiable' => filter_var($event['isNotifiable'], FILTER_VALIDATE_BOOLEAN),
                    'subjectId' => $event['subjectId'],
                    'groupId' => $event['groupId'],
                    'userId' => $event['userId'],
                    'eventTypeId' => $event['eventTypeId'],
                ];
            };
        });
        return $response;
    }

}
