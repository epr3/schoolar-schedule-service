<?php
namespace App\Http\Controllers;

use App\Repositories\SubjectProfessorRepository;
use Illuminate\Http\Request;

class SubjectProfessorController extends Controller
{

    protected $subjectProfessor;

    public function __construct(SubjectProfessorRepository $subjectProfessor)
    {
        $this->subjectProfessor = $subjectProfessor;
    }

    public function store(Request $request)
    {
        $this->validate($request, [
            'userId' => 'required',
            'subjectId' => 'required',
        ]);

        return $this->subjectProfessor->create($request->all());
    }

    public function show($id)
    {
        return $this->subjectProfessor->get($id);
    }

    public function update(Request $request, $id)
    {
        $this->validate($request, [
            'userId' => 'required',
            'subjectId' => 'required',
        ]);

        $this->subjectProfessor->update($request->all(), $id);
        return $this->subjectProfessor->get($id);
    }

    public function delete($id)
    {
        $this->subjectProfessor->delete($id);
        return response(null, 204);
    }

    public function index(Request $request)
    {
        return $this->subjectProfessor->all($request->query());
    }

}
