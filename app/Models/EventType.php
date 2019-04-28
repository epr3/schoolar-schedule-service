<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class EventType extends Model
{
    use UUIDModel;

    protected $fillable = [
        'type', 'color',
    ];
}
