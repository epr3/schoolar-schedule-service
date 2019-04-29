<?php

namespace App\Http\Middleware;

use Closure;
use Exception;
use Firebase\JWT\JWT;
use Firebase\JWT\ExpiredException;

class JWTMiddleware
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle($request, Closure $next)
    {
        $token = $request->headers->get('authorization');

        if (!$token) {
            return response('Unauthorized', 401);
        }
        try {
            $credentials = JWT::decode(explode('JWT ', $token)[1], env('JWT_SECRET'), array('HS256'));
        } catch(ExpiredException $e) {
            return response()->json([
                'message' => 'Provided token is expired.'
            ], 400);
        } catch(Exception $e) {
            dd($e);
            return response()->json([
                'message' => 'An error occured while decoding token.'
            ], 400);
        }
        $request->auth = $credentials->context;
        return $next($request);
    }
}
