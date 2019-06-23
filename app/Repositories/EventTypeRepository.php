<?php namespace App\Repositories;

use App\Models\EventType;

class EventTypeRepository implements RepositoryInterface
{
    public function all($data)
    {
        if (empty($data)) {
            return EventType::all();
        }

        return EventType::where($data)->get();
    }

    public function create(array $data)
    {
        return EventType::create($data);
    }

    public function update(array $data, $id)
    {
        return EventType::find($id)->update($data);
    }

    public function delete($id)
    {
        return EventType::destroy($id);
    }

    public function get($id)
    {
        return EventType::findOrFail($id);
    }

}
