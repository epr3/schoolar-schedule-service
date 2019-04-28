<?php namespace App\Repositories;

use App\Models\Event;

class EventRepository implements RepositoryInterface
{
    public function all()
    {
        return Event::all();
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
