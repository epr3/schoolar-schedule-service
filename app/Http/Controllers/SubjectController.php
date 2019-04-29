<?php
namespace App\Http\Controllers;

use App\Repositories\SubjectRepository;
use Illuminate\Http\Request;

class SubjectController extends Controller
{

    protected $subject;

    public function __construct(SubjectRepository $subject)
    {
        $this->subject = $subject;
    }

    public function store(Request $request)
    {
        $this->validate($request, [
            'name' => 'required',
            'credits' => 'required|integer',
            'facultyId' => 'required',
        ]);

        return $this->subject->create($request->all());
    }

    public function show($id)
    {
        return $this->subject->get($id);
    }

    public function update(Request $request, $id)
    {
        $this->validate($request, [
            'name' => 'required',
            'credits' => 'required|integer',
            'facultyId' => 'required',
        ]);

        $this->subject->update($request->all(), $id);
        return $this->subject->get($id);
    }

    public function delete($id)
    {
        $this->subject->delete($id);
        return response(null, 204);
    }

    public function index(Request $request)
    {
        return $this->subject->all($request->query());
    }

}
