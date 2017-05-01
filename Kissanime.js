// ==UserScript==
// @name         KissAnime
// @namespace    https://houssem.me/
// @version      0.1
// @description  Beta-server/quality changer in kissanime.ru
// @author       Houssem Charfeddine
// @match        http://kissanime.ru/Anime/*
// @require http://code.jquery.com/jquery-latest.js
// ==/UserScript==

$(document).ready(function() {
 if ($("#selectServer").length > 0){
     $("#selectServer > option").each(function() {
         if (this.text=="Beta Server")
             if (!this.selected)
             {
                 $("#selectServer").val(this.value);
                 $("#slcQualix > option").each(function() {
                  if (this.text=="360p")
                      if (!this.selected)
                           $("#slcQualix").val(this.value);
                 });
              }
             
     });

 }
 });










