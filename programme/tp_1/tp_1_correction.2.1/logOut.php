<?php
session_unset();
if (empty($_SESSION)) {
    header('location: ./');
}
