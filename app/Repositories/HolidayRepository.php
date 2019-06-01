<?php namespace App\Repositories;

use App\Models\Holiday;

class HolidayRepository implements RepositoryInterface
{
    public function all($data)
    {
        return Holiday::all();
    }

    public function create(array $data)
    {
        return Holiday::create($data);
    }

    public function update(array $data, $id)
    {
        return Holiday::find($id)->update($data);
    }

    public function delete($id)
    {
        return Holiday::destroy($id);
    }

    public function get($id)
    {
        return Holiday::findOrFail($id);
    }

}
