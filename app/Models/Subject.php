<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Subject extends Model
{
    use UUIDModel;

    protected $fillable = [
        'name', 'credits', 'facultyId',
    ];

    public function professors() {
        return $this->hasMany('App\Models\SubjectProfessor', 'subjectId');
    }
}
