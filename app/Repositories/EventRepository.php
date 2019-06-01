<?php namespace App\Repositories;

use Carbon\Carbon;
use App\Models\Event;


class EventRepository implements RepositoryInterface
{
    public function all($data)
    {
        $eventQuery = [];

        if (empty($data)) {
            return Event::all();
        }
        if (isset($data['startDate'])) {
            array_push($eventQuery, ['endDate', '>=', Carbon::parse($data['startDate'])->toDateString()]);
        }
        if (isset($data['endDate'])) {
            array_push($eventQuery, ['startDate', '<=', Carbon::parse($data['endDate'])->toDateString()]);
        }
        if (isset($data['groupId'])) {
            array_push($eventQuery, ['groupId', '=', $data['groupId']]);
        }
        if (isset($data['userId'])) {
            array_push($eventQuery, ['userId', '=', $data['userId']]);
        }
        return Event::where($eventQuery)->get();
    }

    public function create(array $data)
    {
        return Event::create($data);
    }

    public function update(array $data, $id)
    {
        return Event::find($id)->update($data);
    }

    public function delete($id)
    {
        return Event::destroy($id);
    }

    public function get($id)
    {
        return Event::findOrFail($id);
    }

}
