<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Group extends Model
{
    use UUIDModel;

    protected $fillable = [
        'number', 'year', 'facultyId',
    ];

    public function events() {
        return $this->hasMany('App\Models\Event', 'groupId');
    }
}
