<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Event extends Model
{
    use UUIDModel;

    protected $fillable = [
        'room', 'interval', 'frequency', 'startDate', 'endDate', 'startTime', 'endTime', 'isFullDay', 'isNotifiable', 'subjectId', 'groupId', 'professorId', 'eventTypeId',
    ];
}
