<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It is a breeze. Simply tell Lumen the URIs it should respond to
| and give it the Closure to call when that URI is requested.
|
 */

$router->get('/', function () use ($router) {
    return $router->app->version();
});

$router->get('/healthz', function () {
    return 'OK';
});

$router->get('/faculties', ['middleware' => 'jwt', 'uses' => 'FacultyController@index']);
$router->get('/faculties/{id}', ['middleware' => 'jwt', 'uses' => 'FacultyController@show']);
$router->post('/faculties', ['middleware' => 'jwt', 'uses' => 'FacultyController@store']);
$router->put('/faculties/{id}', ['middleware' => 'jwt', 'uses' => 'FacultyController@update']);
$router->delete('/faculties/{id}', ['middleware' => 'jwt', 'uses' => 'FacultyController@delete']);

$router->get('/courses', ['middleware' => 'jwt', 'uses' => 'CourseController@index']);
$router->get('/courses/{id}', ['middleware' => 'jwt', 'uses' => 'CourseController@show']);
$router->post('/courses', ['middleware' => 'jwt', 'uses' => 'CourseController@store']);
$router->put('/courses/{id}', ['middleware' => 'jwt', 'uses' => 'CourseController@update']);
$router->delete('/courses/{id}', ['middleware' => 'jwt', 'uses' => 'CourseController@delete']);


$router->get('/subjects', ['middleware' => 'jwt', 'uses' => 'SubjectController@index']);
$router->get('/subjects/{id}', ['middleware' => 'jwt', 'uses' => 'SubjectController@show']);
$router->post('/subjects', ['middleware' => 'jwt', 'uses' => 'SubjectController@store']);
$router->put('/subjects/{id}', ['middleware' => 'jwt', 'uses' => 'SubjectController@update']);
$router->delete('/subjects/{id}', ['middleware' => 'jwt', 'uses' => 'SubjectController@delete']);

$router->get('/subject-professors', ['middleware' => 'jwt', 'uses' => 'SubjectProfessorController@index']);
$router->get('/subject-professors/{id}', ['middleware' => 'jwt', 'uses' => 'SubjectProfessorController@show']);
$router->post('/subject-professors', ['middleware' => 'jwt', 'uses' => 'SubjectProfessorController@store']);
$router->put('/subject-professors/{id}', ['middleware' => 'jwt', 'uses' => 'SubjectProfessorController@update']);
$router->delete('/subject-professors/{id}', ['middleware' => 'jwt', 'uses' => 'SubjectProfessorController@delete']);


$router->get('/events', ['middleware' => 'jwt', 'uses' => 'EventController@index']);
$router->get('/events/{id}', ['middleware' => 'jwt', 'uses' => 'EventController@show']);
$router->post('/events', ['middleware' => 'jwt', 'uses' => 'EventController@store']);
$router->put('/events/{id}', ['middleware' => 'jwt', 'uses' => 'EventController@update']);
$router->delete('/events/{id}', ['middleware' => 'jwt', 'uses' => 'EventController@delete']);

$router->get('/groups', ['middleware' => 'jwt', 'uses' => 'GroupController@index']);
$router->get('/groups/{id}', ['middleware' => 'jwt', 'uses' => 'GroupController@show']);
$router->post('/groups', ['middleware' => 'jwt', 'uses' => 'GroupController@store']);
$router->put('/groups/{id}', ['middleware' => 'jwt', 'uses' => 'GroupController@update']);
$router->delete('/groups/{id}', ['middleware' => 'jwt', 'uses' => 'GroupController@delete']);

$router->get('/event_types', ['middleware' => 'jwt', 'uses' => 'EventTypeController@index']);
$router->get('/event_types/{id}', ['middleware' => 'jwt', 'uses' => 'EventTypeController@show']);
$router->post('/event_types', ['middleware' => 'jwt', 'uses' => 'EventTypeController@store']);
$router->put('/event_types/{id}', ['middleware' => 'jwt', 'uses' => 'EventTypeController@update']);
$router->delete('/event_types/{id}', ['middleware' => 'jwt', 'uses' => 'EventTypeController@delete']);

$router->get('/courses', ['middleware' => 'jwt', 'uses' => 'CourseController@index']);
$router->post('/courses', ['middleware' => 'jwt', 'uses' => 'CourseController@store']);
$router->put('/courses/{id}', ['middleware' => 'jwt', 'uses' => 'CourseController@update']);
$router->delete('/courses/{id}', ['middleware' => 'jwt', 'uses' => 'CourseController@delete']);

$router->get('/holidays', ['middleware' => 'jwt', 'uses' => 'HolidayController@index']);
$router->post('/holidays', ['middleware' => 'jwt', 'uses' => 'HolidayController@store']);
$router->put('/holidays/{id}', ['middleware' => 'jwt', 'uses' => 'HolidayController@update']);
$router->delete('/holidays/{id}', ['middleware' => 'jwt', 'uses' => 'HolidayController@delete']);

