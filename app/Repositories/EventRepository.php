<?php namespace App\Repositories;

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
            array_push($eventQuery, ['startDate', '>=', $data['startDate']]);
        }
        if (isset($data['endDate'])) {
            array_push($eventQuery, ['endDate', '<=', $data['endDate']]);
        }
        if (isset($data['groupId'])) {
            array_push($eventQuery, ['groupId', '=', $data['groupId']]);
        }
        if (isset($data['professorId'])) {
            array_push($eventQuery, ['professorId', '=', $data['professorId']]);
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
