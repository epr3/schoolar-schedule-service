<?php namespace App\Repositories;

use App\Models\Subject;

class SubjectRepository implements RepositoryInterface
{
    public function all()
    {
        return Subject::all();
    }

    public function create(array $data)
    {
        return Subject::create($data);
    }

    public function update(array $data, $id)
    {
        return Subject::find($id)->update($data);
    }

    public function delete($id)
    {
        return Subject::destroy($id);
    }

    public function get($id)
    {
        return Subject::findOrFail($id);
    }

}
