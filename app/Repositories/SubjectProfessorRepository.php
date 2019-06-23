<?php namespace App\Repositories;

use App\Models\SubjectProfessor;

class SubjectProfessorRepository implements RepositoryInterface
{
    public function all($data)
    {
        if (empty($data)) {
            return SubjectProfessor::all();

        }
        return SubjectProfessor::where($data)->get();

    }

    public function create(array $data)
    {
        return SubjectProfessor::create($data);
    }

    public function update(array $data, $id)
    {
        return SubjectProfessor::find($id)->update($data);
    }

    public function delete($id)
    {
        return SubjectProfessor::destroy($id);
    }

    public function get($id)
    {
        return SubjectProfessor::findOrFail($id);
    }

}
