<?php
     $page_num = 1;
     $txtString = "";
     while ($page_num <= 10 )
     {
         $host = "http://search.twitter.com/search.atom?q=from%3Aplomlompom";
         $result = file_get_contents($host);
         $xml = new SimpleXMLElement($result);
         foreach ($xml->entry as $entry)
         {
          $statusUpdate[] = $entry->title;
         }
       $page_num++;
     }
     foreach($statusUpdate as $su)
     {
       $txtString .= $su . "\n";
     }

     $myFile = "myTextFile.txt";
     $fh = fopen($myFile, 'w') or die("can't open file");
     fwrite($fh, $stringData);
     $stringData = $txtString;
     fwrite($fh, $stringData);
     fclose($fh);
?> 

