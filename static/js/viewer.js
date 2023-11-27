const nombreSala = localStorage.getItem('nombreSalaSeleccionada') || [];
var interfaceConfig = {

    TOOLBAR_BUTTONS: [
        //'microphone',           //Activar Microfono
        //'camera',               //Activar Camara
        //'closedcaptions',     //mostrar subtítulos
        //'desktop',              //Compartir pantalla
        //'fullscreen',           //Pantalla Completa
        //'fodeviceselection',    //Seleccion de dispositivos de audios y videos
        //'hangup',                //SAlir
        //'profile',
        // 'info',               //ver el link
        //'chat',
        //'recording',             //grabar
        //'livestreaming',      //admin lo puede hacer
        //'etherpad',           //Edicion de documentos
        // 'sharedvideo',        //admin lo puede hacer
        //'settings',             //Config de la reunion
        //'raisehand',              //manito
        //'videoquality',           //calidad de video
        //'filmstrip',          //miniatura de los participantes
        //'invite',               //invita a otros a la reunion
        //'feedback',           //Los usuarios dan una retroalimentacion o comentarios durante la reunion
        //'stats',                //estadísticas de la reunión, como datos de rendimiento
        //'shortcuts',          //atajos de teclado
        //'tileview',           //vista que muestra a todos los participantes en mosaico
        //'videobackgroundblur',//desenfocar su fondo de video
        //'download',           //descargar grabaciones o archivos compartidos durante la reunión.
        //'help',               
        //'mute-everyone',    //administrador
        'e2ee'                  //Cifrado de extremo a extremo
    ],

    SETTINGS_SECTIONS: [

    ],
    SHOW_CHROME_EXTENSION_BANNER: false
};

const domain = 'meet.jit.si';

const options = {
    roomName: nombreSala,
    width: '100%',
    height: 850,
    parentNode: document.querySelector('#meet'),
    userInfo: {
        email: "viewers@gmail.com",
        displayName: "viewers",
        role: 'participant'
    },
    noSsl: true,
    interfaceConfigOverwrite: interfaceConfig,
};
const api = new JitsiMeetExternalAPI(domain, options);