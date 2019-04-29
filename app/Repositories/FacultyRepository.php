<?php namespace App\Repositories;

use Illuminate\Database\Eloquent\Model;
use App\Models\Faculty;

class FacultyRepository implements RepositoryInterface
{
    public function all($data)
    {
        return Faculty::all();
    }

    public function create(array $data)
    {
        return Faculty::create($data);
    }

    public function update(array $data, $id)
    {
        return Faculty::find($id)->update($data);
    }

    public function delete($id)
    {
        return Faculty::destroy($id);
    }

    public function get($id)
    {
        return Faculty::findOrFail($id);
    }

}
