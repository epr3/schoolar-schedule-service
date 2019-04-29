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
            'professorId' => 'required',
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
            'professorId' => 'required',
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
        $response = [];
        $eventList = $this->event->all($request->query());
        if (is_null($request->query('startDate')) && is_null($request->query('endDate'))) {
            return $eventList->load('group', 'subject', 'eventType');
        }
        foreach ($eventList as $event) {
            foreach (new RRule([
                'FREQ' => $event['frequency'],
                'DTSTART' => $event['startDate'],
                'UNTIL' => $event['endDate'],
                'INTERVAL' => $event['interval'],
            ]) as $occurence) {

                array_push($response, [
                    'date' => Carbon::parse($occurence)->toDateString(),
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
        return $response;
    }

}
