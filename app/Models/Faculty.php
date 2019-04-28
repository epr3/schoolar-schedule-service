<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Faculty extends Model
{
    use UUIDModel;

    protected $fillable = [
        'name'
    ];
}
