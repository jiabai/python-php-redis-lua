import redis

script1 = '''local uid = KEYS[1] \
          local field = "m:v" \
          local vv = cjson.decode(ARGV[1]) \
          local msgpack = cmsgpack.pack(vv) \
          return redis.call("hset", uid, field, msgpack)'''
script1 = '''local uid = KEYS[1] \
          local v = ARGV[1] \
          local t = tonumber(ARGV[2]) \
          local vv = {["v"]=ARGV[1], ["t"]=ARGV[2], ["tp"]="1", ["pt"] = "174"} \
          return type(t)'''

script2 = '''local uid = KEYS[1] \
          local v = ARGV[1] \
          local t = tonumber(ARGV[2]) \
          local msgpack = redis.call("hget", uid, "m:v") \
          if msgpack ~= false then \
            local vv = cmsgpack.unpack(msgpack) \
            local mv = {["v"]=v, ["t"]=t, ["tp"]="1", ["pt"] = "174"} \
            table.insert(vv, mv) \
            msgpack = cmsgpack.pack(vv) \
          else \
            local vv = {}
            table.insert(vv, {["v"]=v, ["t"]=t, ["tp"]="1", ["pt"] = "174"}) \
            msgpack = cmsgpack.pack(vv) \
          end \
          return redis.call("hset", uid, "m:v", msgpack)'''

script3 = '''local uid = KEYS[1] \
          local msgpack = redis.call("hget", uid, "m:v") \
          local vv = cmsgpack.unpack(msgpack) \
          return cjson.encode(vv)'''

r = redis.StrictRedis(host='192.168.3.131', port=11211, db=0)
#multiply = r.register_script(script2)
#print multiply(keys=['{91B3B6E8858B-5EE5-080B-C845-6E8858B}'], args=["7760081550325", 1397821753])
#print multiply(keys=['{761C6DCB-5EE5-080B-C845-91B3B6E8858B}'], args=["7760081550325", 1397821753])
#multiply = r.register_script(script3)
#print multiply(keys=['241EA034-37C1-4B49-9F59-BA2B76A59CDE'])
print r.eval(script3, 1, '241EA034-37C1-4B49-9F59-BA2B76A59CDE')
#print multiply(keys=['{761C6DCB-5EE5-080B-C845-91B3B6E8858B}'])

