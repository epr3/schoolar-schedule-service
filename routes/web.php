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

$router->get('/faculties', 'FacultyController@index');
$router->post('/faculties', 'FacultyController@store');
$router->put('/faculties/{id}', 'FacultyController@update');
$router->delete('/faculties/{id}', 'FacultyController@delete');

$router->get('/subjects', 'SubjectController@index');
$router->post('/subjects', 'SubjectController@store');
$router->put('/subjects/{id}', 'SubjectController@update');
$router->delete('/subjects/{id}', 'SubjectController@delete');

$router->get('/events', 'EventController@index');
$router->post('/events', 'EventController@store');
$router->put('/events/{id}', 'EventController@update');
$router->delete('/events/{id}', 'EventController@delete');

$router->get('/groups', 'GroupController@index');
$router->post('/groups', 'GroupController@store');
$router->put('/groups/{id}', 'GroupController@update');
$router->delete('/groups/{id}', 'GroupController@delete');

$router->get('/event_types', 'EventTypeController@index');
$router->post('/event_types', 'EventTypeController@store');
$router->put('/event_types/{id}', 'EventTypeController@update');
$router->delete('/event_types/{id}', 'EventTypeController@delete');

$router->get('/courses', 'CourseController@index');
$router->post('/courses', 'CourseController@store');
$router->put('/courses/{id}', 'CourseController@update');
$router->delete('/courses/{id}', 'CourseController@delete');
