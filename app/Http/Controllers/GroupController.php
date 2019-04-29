<?php
namespace App\Http\Controllers;

use App\Repositories\GroupRepository;
use Illuminate\Http\Request;

class GroupController extends Controller
{

    protected $group;

    public function __construct(GroupRepository $group)
    {
        $this->group = $group;
    }

    public function store(Request $request)
    {
        $this->validate($request, [
            'number' => 'required',
            'year' => 'required',
            'facultyId' => 'required',
        ]);

        return $this->group->create($request->all());
    }

    public function show($id)
    {
        return $this->group->get($id);
    }

    public function update(Request $request, $id)
    {
        $this->validate($request, [
            'number' => 'required',
            'year' => 'required',
            'facultyId' => 'required',
        ]);

        $this->group->update($request->all(), $id);
        return $this->group->get($id);
    }

    public function delete($id)
    {
        $this->group->delete($id);
        return response(null, 204);
    }

    public function index(Request $request)
    {
        return $this->group->all($request->query())->load('events');
    }

}
