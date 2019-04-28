<?php
namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Repositories\FacultyRepository;

class FacultyController extends Controller
{

    protected $faculty;

    public function __construct(FacultyRepository $faculty)
    {
        $this->faculty = $faculty;
    }

    public function store(Request $request) {
        return $this->faculty->create($request->all());
    }

    public function show($id) {}

    public function update(Request $request, $id) {}

    public function delete(Request $request, $id) {}

    public function index()
    {
        return $this->faculty->all();
    }

}
