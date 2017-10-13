// ==UserScript==
// @name         Pandora_still_listening
// @namespace    http://houssem.me/
// @version      0.1
// @description  I am still listening button
// @author       Houssem Charfeddine
// @match        https://www.pandora.com/*
// @require http://code.jquery.com/jquery-latest.js
// ==/UserScript==
$( document ).ready(function() {
$(".StillListeningBody__subtitle").ready(function() {
 $('button[data-qa="keep_listening_button"]').trigger('click');
     });
});