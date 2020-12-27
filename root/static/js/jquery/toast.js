var Toast = {
	show: function (msg)
	{ 
		cordova.exec(this.onSuccess, this.onFail, "Toast", "nativeAction", [msg]);
    },
	onSuccess:function  (result)
	{ 
	} ,
	onFail: function  (error)
	{ 
		alert("ERROR: \r\n" + error); 
	}
} ;

