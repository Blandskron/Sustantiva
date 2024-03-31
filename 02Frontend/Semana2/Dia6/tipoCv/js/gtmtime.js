function mostrarHora() {
			// Obtener la hora actual en diferentes zonas horarias
			var horaGTM0 = new Date().toUTCString();
			var horaGTM1 = new Date(new Date().getTime() + 3600000).toUTCString();
			var horaGTM2 = new Date(new Date().getTime() + 7200000).toUTCString();
            var horaGTM3 = new Date(new Date().getTime() + 10800000).toUTCString();
			var horaGTM4 = new Date(new Date().getTime() + 14400000).toUTCString();
			var horaGTM5 = new Date(new Date().getTime() + 18000000).toUTCString();
            var horaGTM6 = new Date(new Date().getTime() + 21600000).toUTCString();
			var horaGTM7 = new Date(new Date().getTime() + 25200000).toUTCString();
			var horaGTM8 = new Date(new Date().getTime() + 28800000).toUTCString();
            var horaGTM9 = new Date(new Date().getTime() + 32400000).toUTCString();
			var horaGTM10 = new Date(new Date().getTime() + 36000000).toUTCString();
			var horaGTM11 = new Date(new Date().getTime() + 39600000).toUTCString();
            var horaGTM12 = new Date(new Date().getTime() + 43200000).toUTCString();
			var horaGTM_1 = new Date(new Date().getTime() - 3600000).toUTCString();
			var horaGTM_2 = new Date(new Date().getTime() - 7200000).toUTCString();
			var horaGTM_3 = new Date(new Date().getTime() - 10800000).toUTCString();
			var horaGTM_4 = new Date(new Date().getTime() - 14400000).toUTCString();
			var horaGTM_5 = new Date(new Date().getTime() - 18000000).toUTCString();
			var horaGTM_6 = new Date(new Date().getTime() - 21600000).toUTCString();
			var horaGTM_7 = new Date(new Date().getTime() - 25200000).toUTCString();
			var horaGTM_8 = new Date(new Date().getTime() - 28800000).toUTCString();
			var horaGTM_9 = new Date(new Date().getTime() - 32400000).toUTCString();
			var horaGTM_10 = new Date(new Date().getTime() - 36000000).toUTCString();
			var horaGTM_11 = new Date(new Date().getTime() - 39600000).toUTCString();
			var horaGTM_12 = new Date(new Date().getTime() - 43200000).toUTCString();

			// Actualizar el contenido de los elementos con la hora
			document.getElementById("hora-gtm0").innerHTML = horaGTM0;
			document.getElementById("hora-gtm1").innerHTML = horaGTM1;
			document.getElementById("hora-gtm2").innerHTML = horaGTM2;
            document.getElementById("hora-gtm3").innerHTML = horaGTM3;
			document.getElementById("hora-gtm4").innerHTML = horaGTM4;
			document.getElementById("hora-gtm5").innerHTML = horaGTM5;
			document.getElementById("hora-gtm6").innerHTML = horaGTM6;
            document.getElementById("hora-gtm7").innerHTML = horaGTM7;
			document.getElementById("hora-gtm8").innerHTML = horaGTM8;
			document.getElementById("hora-gtm9").innerHTML = horaGTM9;
			document.getElementById("hora-gtm10").innerHTML = horaGTM10;
			document.getElementById("hora-gtm11").innerHTML = horaGTM11;
            document.getElementById("hora-gtm12").innerHTML = horaGTM12;
            document.getElementById("hora-gtm-1").innerHTML = horaGTM_1;
            document.getElementById("hora-gtm-2").innerHTML = horaGTM_2;
			document.getElementById("hora-gtm-3").innerHTML = horaGTM_3;
			document.getElementById("hora-gtm-4").innerHTML = horaGTM_4;
            document.getElementById("hora-gtm-5").innerHTML = horaGTM_5;
			document.getElementById("hora-gtm-6").innerHTML = horaGTM_6;
			document.getElementById("hora-gtm-7").innerHTML = horaGTM_7;
			document.getElementById("hora-gtm-8").innerHTML = horaGTM_8;
			document.getElementById("hora-gtm-9").innerHTML = horaGTM_9;
            document.getElementById("hora-gtm-10").innerHTML = horaGTM_10;
            document.getElementById("hora-gtm-11").innerHTML = horaGTM_11;
            document.getElementById("hora-gtm-12").innerHTML = horaGTM_12;
			
			
		}

		// Actualizar la hora cada segundo
		setInterval(mostrarHora, 1000);