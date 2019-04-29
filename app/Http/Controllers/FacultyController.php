<?php
namespace App\Http\Controllers;

use App\Repositories\FacultyRepository;
use Illuminate\Http\Request;

class FacultyController extends Controller
{

    protected $faculty;

    public function __construct(FacultyRepository $faculty)
    {
        $this->faculty = $faculty;
    }

    public function store(Request $request)
    {
        $this->validate($request, [
            'name' => 'required',
        ]);

        return $this->faculty->create($request->all());
    }

    public function show($id)
    {
        return $this->faculty->get($id);
    }

    public function update(Request $request, $id)
    {
        $this->validate($request, [
            'name' => 'required',
        ]);

        $this->faculty->update($request->all(), $id);
        return $this->faculty->get($id);
    }

    public function delete($id)
    {
        $this->faculty->delete($id);
        return response(null, 204);
    }

    public function index()
    {
        return $this->faculty->all(null);
    }

}
