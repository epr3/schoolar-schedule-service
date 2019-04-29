<?php namespace App\Repositories;

use App\Models\Course;

class CourseRepository implements RepositoryInterface
{
    public function all($data)
    {
        return Course::all();
    }

    public function create(array $data)
    {
        return Course::create($data);
    }

    public function update(array $data, $id)
    {
        return Course::find($id)->update($data);
    }

    public function delete($id)
    {
        return Course::destroy($id);
    }

    public function get($id)
    {
        return Course::findOrFail($id);
    }

}
