
$(document).ready(function(){
    //Update the player list using values from other dropdowns to make an ajax
    //query which returns the allowed values
    function updatePlayerList() {
        var pos = $('select[name=pos] option:selected').text();
        var club = $('select[name=club] option:selected').text();
        console.log("UpdatePlayerList: " + pos + " " + club);

        // Clear and disable player names
        $('#names').html('');
        $('#names').attr('disabled', 'disabled');

        // If both a position and club have been specified then find the
        // corresponding player list
        if (pos != '' && club != '') {
            $.ajax({
                url: '/getplayers.json',
                data: 'unowned=1&pos=' + pos + '&club=' + club,
                dataType: 'json',
                success: function(data) {
                    var listItems= "<option></option>";
                    console.log("UpdatePlayerList: " + data[0]);

                    for (var i in data) {
                        listItems += '<option name=\"' + data[i] + '\">' +
                                         data[i] + '</option>';
                    }
                    $('#names').removeAttr('disabled');
                    $('#names').html(listItems)
               }
            });
        }
    }

    //If the position changes then clear everything and update the player list
    $('select[name=pos]').change(function() {
        updatePlayerList();
    });

    //If the club changes then clear everything and update the player list
    $('select[name=club]').change(function() {
        updatePlayerList();
    });

    // Start by updating the player list on page load
    updatePlayerList();
});
