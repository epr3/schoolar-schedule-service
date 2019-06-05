<?php
namespace App\Http\Controllers;

use App\Repositories\CourseRepository;
use Illuminate\Http\Request;

class CourseController extends Controller
{

    protected $course;

    public function __construct(CourseRepository $course)
    {
        $this->course = $course;
    }

    public function store(Request $request)
    {
        $this->validate($request, [
            'name' => 'required',
            'coursePath' => 'required',
            'userId' => 'required',
            'subjectId' => 'required',
            'courseFilename' => 'required',
        ]);
        return $this->course->create($request->all());
    }

    public function show($id)
    {
        return $this->course->get($id);
    }

    public function update(Request $request, $id)
    {
        $this->validate($request, [
            'name' => 'required',
            'coursePath' => 'required',
            'userId' => 'required',
            'subjectId' => 'required',
            'courseFilename' => 'required',
        ]);

        $this->course->update($request->all(), $id);
        return $this->course->get($id);
    }

    public function delete($id)
    {
        $this->course->delete($id);
        return response(null, 204);
    }

    public function index(Request $request)
    {
        return $this->course->all($request->query());
    }

}
