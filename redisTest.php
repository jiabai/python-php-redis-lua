<?php
$script1 = 'local uid = KEYS[1]'
  .' local field = "m:v"'
  .' local vv = cjson.decode(ARGV[1])'
  .' local msgpack = cmsgpack.pack(vv)'
  .' return redis.call("hset", uid, field, msgpack)';

$script2 = 'local msgpack = redis.call("hget", KEYS[1], "m:v")'
  .' local vv = cmsgpack.unpack(msgpack)'
  .' local mv = {["v"]=ARGV[1], ["t"]=ARGV[2], ["tp"]="1", ["pt"] = "174"}'
  .' table.insert(vv, mv)'
  .' return cjson.encode(vv)';

$uid = "{761C6DCB-5EE5-080B-C845-91B3B6E8858B}";

$item1 = array("v"=>"775121_114496_1576418", "t"=>1405963695, "tp"=>"1", "pt"=>"174");
$item2 = array("v"=>"215006_36450_450786", "t"=>1399645033, "tp"=>"2", "pt"=>"23");
$item3 = array("v"=>"111910_50563_664984", "t"=>1397821753, "tp"=>"1", "pt"=>"1688");
$item4 = array("v"=>"776008_112964_1550325", "t"=>1397754246, "tp"=>"1", "pt"=>"1372");
$vv = array($item1, $item2, $item3, $item4);
$vv = json_encode($vv);

$mid = "95121_114496_15764";
$ts  = 1405763695;

$redis = new Redis();
$redis->connect("127.0.0.1", 6379);
/*
$sha = $redis->script("load", $script1);
echo $redis->evalSha($sha, Array($uid, $vv), 1);
echo "\n";
*/

$sha = $redis->script("load", $script2);
$ret = $redis->evalSha($sha, Array($uid, $mid, $ts), 1);
echo $ret;
echo "\n";
?>
