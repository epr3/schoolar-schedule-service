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
            'course_path' => 'required',
            'subjectId' => 'required',
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
            'course_path' => 'required',
            'subjectId' => 'required',
        ]);

        $this->course->update($request->all(), $id);
        return $this->course->get($id);
    }

    public function delete($id)
    {
        $this->course->delete($id);
        return response(null, 204);
    }

    public function index()
    {
        return $this->course->all();
    }

}
