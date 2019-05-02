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
$router->post('/faculties', ['middleware' => 'jwt', 'uses' => 'FacultyController@store']);
$router->put('/faculties/{id}', ['middleware' => 'jwt', 'uses' => 'FacultyController@update']);
$router->delete('/faculties/{id}', ['middleware' => 'jwt', 'uses' => 'FacultyController@delete']);

$router->get('/subjects', ['middleware' => 'jwt', 'uses' => 'SubjectController@index']);
$router->post('/subjects', ['middleware' => 'jwt', 'uses' => 'SubjectController@store']);
$router->put('/subjects/{id}', ['middleware' => 'jwt', 'uses' => 'SubjectController@update']);
$router->delete('/subjects/{id}', ['middleware' => 'jwt', 'uses' => 'SubjectController@delete']);

$router->get('/events', ['middleware' => 'jwt', 'uses' => 'EventController@index']);
$router->post('/events', ['middleware' => 'jwt', 'uses' => 'EventController@store']);
$router->put('/events/{id}', ['middleware' => 'jwt', 'uses' => 'EventController@update']);
$router->delete('/events/{id}', ['middleware' => 'jwt', 'uses' => 'EventController@delete']);

$router->get('/groups', ['middleware' => 'jwt', 'uses' => 'GroupController@index']);
$router->get('/groups/{id}', ['middleware' => 'jwt', 'uses' => 'GroupController@show']);
$router->post('/groups', ['middleware' => 'jwt', 'uses' => 'GroupController@store']);
$router->put('/groups/{id}', ['middleware' => 'jwt', 'uses' => 'GroupController@update']);
$router->delete('/groups/{id}', ['middleware' => 'jwt', 'uses' => 'GroupController@delete']);

$router->get('/event_types', ['middleware' => 'jwt', 'uses' => 'EventTypeController@index']);
$router->post('/event_types', ['middleware' => 'jwt', 'uses' => 'EventTypeController@store']);
$router->put('/event_types/{id}', ['middleware' => 'jwt', 'uses' => 'EventTypeController@update']);
$router->delete('/event_types/{id}', ['middleware' => 'jwt', 'uses' => 'EventTypeController@delete']);

$router->get('/courses', ['middleware' => 'jwt', 'uses' => 'CourseController@index']);
$router->post('/courses', ['middleware' => 'jwt', 'uses' => 'CourseController@store']);
$router->put('/courses/{id}', ['middleware' => 'jwt', 'uses' => 'CourseController@update']);
$router->delete('/courses/{id}', ['middleware' => 'jwt', 'uses' => 'CourseController@delete']);
