<?php
namespace App\Http\Controllers;

use App\Repositories\HolidayRepository;
use Illuminate\Http\Request;

class HolidayController extends Controller
{

    protected $holiday;

    public function __construct(HolidayRepository $holiday)
    {
        $this->holiday = $holiday;
    }

    public function store(Request $request)
    {
        $this->validate($request, [
            'startDate' => 'required|date',
            'endDate' => 'required|date',
            'name' => 'required',
        ]);
        return $this->holiday->create($request->all());
    }

    public function show($id)
    {
        return $this->holiday->get($id);
    }

    public function update(Request $request, $id)
    {
        $this->validate($request, [
            'startDate' => 'required|date',
            'endDate' => 'required|date',
            'name' => 'required',
        ]);

        $this->holiday->update($request->all(), $id);
        return $this->holiday->get($id);
    }

    public function delete($id)
    {
        $this->holiday->delete($id);
        return response(null, 204);
    }

    public function index()
    {
        return $this->holiday->all(null);
    }

}
