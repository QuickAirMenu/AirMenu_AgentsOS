<?php
/**
 * Plugin Name: REVAL Old URL Redirects
 * Description: 301 redirects for legacy URLs that no longer resolve (old Arabic-encoded slugs).
 */

add_action('template_redirect', function () {
    $uri = isset($_SERVER['REQUEST_URI']) ? trim($_SERVER['REQUEST_URI']) : '';
    $uri = rawurldecode($uri);
    $uri = rtrim($uri, '/');

    $map = array(
        '/ar/' . rawurldecode('%d8%a5%d9%86%d8%b6%d9%85-%d8%a5%d9%84%d9%8a%d9%86%d8%a7') => 'https://reval-sa.com/ar/join-us/',
    );

    foreach ($map as $from => $to) {
        if (strcasecmp($uri, $from) === 0) {
            wp_redirect($to, 301);
            exit;
        }
    }
});