
// To verify the map function
var map = function() {
	emit(this.system_id, this.datetime_local);
};

var emit = function(key, value){
	print("emit");
	print("kyes:" + key + "value:" + tojson(value));
};

var sample = db.energy.findOne({system_id: 45});
map.apply(sample);