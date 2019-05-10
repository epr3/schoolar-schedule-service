<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Event extends Model
{
    use UUIDModel;

    protected $casts = [
        'isFullDay' => 'boolean',
        'isNotifiable' => 'boolean',
    ];

    protected $fillable = [
        'room',
        'interval',
        'frequency',
        'startDate',
        'endDate',
        'startTime',
        'endTime',
        'isFullDay',
        'isNotifiable',
        'subjectId',
        'groupId',
        'professorId',
        'eventTypeId',
    ];

    public function subject() {
        return $this->belongsTo('App\Models\Subject', 'subjectId');
    }

    public function group() {
        return $this->belongsTo('App\Models\Group', 'groupId');
    }

    public function eventType() {
        return $this->belongsTo('App\Models\EventType', 'eventTypeId');
    }
}
