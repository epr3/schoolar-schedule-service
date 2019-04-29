<?php
namespace App\Repositories;

use App\Models\Group;

class GroupRepository implements RepositoryInterface
{
    public function all($data)
    {
        if (empty($data)) {
            return Group::all();
        }
        return Group::where($data)->get();

    }

    public function create(array $data)
    {
        return Group::create($data);
    }

    public function update(array $data, $id)
    {
        return Group::find($id)->update($data);
    }

    public function delete($id)
    {
        return Group::destroy($id);
    }

    public function get($id)
    {
        return Group::findOrFail($id);
    }

}
