<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateEventsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('events', function (Blueprint $table) {
            $table->uuid('id')->primary();
            $table->string('room');
            $table->integer('interval');
            $table->string('frequency');
            $table->date('startDate');
            $table->date('endDate');
            $table->time('startTime');
            $table->time('endTime');
            $table->boolean('isFullDay');
            $table->boolean('isNotifiable');
            $table->uuid('subjectId');
            $table->uuid('groupId');
            $table->uuid('eventTypeId');
            $table->foreign('subjectId')
                ->references('id')->on('subjects')
                ->onDelete('cascade');
            $table->foreign('groupId')
                ->references('id')->on('groups')
                ->onDelete('cascade');
            $table->foreign('eventTypeId')
                ->references('id')->on('event_types')
                ->onDelete('cascade');
            $table->string('userId');

            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('events');
    }
}
