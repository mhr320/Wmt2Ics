
    //ydd 06/17/15: jquery UI dialog for confirmation dialog
function cnfrmMsg(title, msg, yesFunc, noFunc) {

    var varDialogText = msg;

    $("#confirmationText").html(varDialogText);

    //bring up the confirmation dialog as modal dialog:
    $("#confirmationDialog").dialog({
        title: title,
        autoopen: false,
        resizable: false,
        width: '500',
        modal: true,
        position: {
            my: "center",
            at: "center",
            of: $("body"),
            within: $("body")
        },
        buttons: {
            "Yes": function () {
                $(this).dialog("close");
                yesFunc();

            },
            "No": function () {
                $(this).dialog("close");
                noFunc();
            }
        }

    });

}

//WS-885: Add function confirmCancelMsg to handle additional "Cancel" button....ydd 08/18/15
   function confirmCancelMsg(title, msg, yesFunc, noFunc, cancelFunc) {

    var varDialogText = msg;

    $("#confirmationText").html(varDialogText);

    //bring up the confirmation dialog as modal dialog:
    $("#confirmationDialog").dialog({
        title: title,
        autoopen: false,
        resizable: false,
        width: '500',
        modal: true,
        position: {
            my: "center",
            at: "center",
            of: $("body"),
            within: $("body")
        },
        buttons: {
            "Yes": function () {
                $(this).dialog("close");
                yesFunc();

            },
            "No": function () {
                $(this).dialog("close");
                noFunc();
            },
             "Cancel": function () {
                $(this).dialog("close");
                cancelFunc();
            }
        }

    });

   
}