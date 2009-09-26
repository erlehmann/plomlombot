<?php
     $page_num = 1;
     $txtString = "";
     while ($page_num <= 10 )
     {
         $host = "http://search.twitter.com/search.atom?q=from%3Aplomlompom&page=$page_num&rpp=100";
         $result = file_get_contents($host);
         $xml = new SimpleXMLElement($result);
         foreach ($xml->entry as $entry)
         {
          echo $entry->title . "\n";
         }
       $page_num++;
     }
?> 

