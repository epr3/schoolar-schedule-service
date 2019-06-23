<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SubjectProfessor extends Model
{
    use UUIDModel;

    protected $fillable = [
        'userId',
        'subjectId',
    ];
}
