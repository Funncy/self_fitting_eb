$(function () {
    $('.goPage1').on('click', function () {
        $('.page2').hide();
        $('.page1').show();
    });

    $('.goPage2').on('click', function () {
        $('.page1').hide();
        $('.page3').hide();
        $('.page2').show();
    });

    $('.goPage3').on('click', function () {

        var isError = false;
        //아동이름 체크
        if (document.getElementById("id_kid_name").value == "") {
            document.getElementById("error_kid_name").innerHTML = "<strong>아동이름을 입력해주세요.</strong>";
            isError = true;
        } else {
            document.getElementById("error_kid_name").innerHTML = "";
        }
        //법정대리인 체크
        if (document.getElementById("id_parent_name").value == "") {
            document.getElementById("error_parent_name").innerHTML = "<strong>법정대리인을 입력해주세요.</strong>";
            isError = true;
        } else {
            document.getElementById("error_parent_name").innerHTML = "";
        }
        //거주지 체크
        if (document.getElementById("id_location").value == "") {
            document.getElementById("error_location").innerHTML = "<strong>거주지를 입력해주세요.</strong>";
            isError = true;
        } else {
            document.getElementById("error_location").innerHTML = "";
        }

        // //생년월일 체크
        // if (document.getElementById("id_birthdate").value == "") {
        //     document.getElementById("error_birthdate").innerHTML = "<strong>생년월일을 입력해주세요.</strong>";
        //     isError = true;
        // } else if (isNaN(Date.parse(document.getElementById("id_birthdate").value))) {
        //     document.getElementById("error_birthdate").innerHTML = "<strong>잘못된 입력입니다.</strong>";
        //     isError = true;
        // } else {
        //     document.getElementById("error_birthdate").innerHTML = "";
        // }
        //연락처 체크
        if (document.getElementById("id_phone_number").value == "") {
            document.getElementById("error_phone_number").innerHTML = "<strong>연락처를 입력해주세요.</strong>";
            isError = true;
        } else {
            document.getElementById("error_phone_number").innerHTML = "";
        }
        //키 체크
        if (document.getElementById("id_height").value == "") {
            document.getElementById("error_height").innerHTML = "<strong>아동의 키를 입력해주세요.</strong>";
            isError = true;
        } else {
            document.getElementById("error_height").innerHTML = "";
        }
        //몸무게 체크
        if (document.getElementById("id_weight").value == "") {
            document.getElementById("error_weight").innerHTML = "<strong>아동의 몸무게를 입력해주세요.</strong>";
            isError = true;
        } else {
            document.getElementById("error_weight").innerHTML = "";
        }

        if ($('input:checkbox[id="id_check1"]').is(":checked") != true) {
            document.getElementById("error_check1").innerHTML = "<strong>동의를 해주셔야합니다.</strong>";
            alert('동의를 해주셔야합니다.');
            isError = true;
        } else {
            document.getElementById("error_check1").innerHTML = "";
        }
        if ($('input:checkbox[id="id_check2"]').is(":checked") != true) {
            document.getElementById("error_check2").innerHTML = "<strong>동의를 해주셔야합니다.</strong>";
            alert('동의를 해주셔야합니다.');
            isError = true;
        } else {
            document.getElementById("error_check2").innerHTML = "";
        }

        if (isError == true) {
            return;
        }

        $('.page2').hide();
        $('.page3').show();
    });

    $('.finish').on('click', function () {

        var isError = false;
        //좌폭 체크
        if (document.getElementById("id_chair_width").value == "") {
            document.getElementById("error_chair_width").innerHTML = "<strong>좌폭을 입력해주세요.</strong>";
            isError = true;
        } else {
            document.getElementById("error_chair_width").innerHTML = "";
        }
        //등 높이 체크
        if (document.getElementById("id_back_height").value == "") {
            document.getElementById("error_back_height").innerHTML = "<strong>등 높이를 입력해주세요.</strong>";
            isError = true;
        } else {
            document.getElementById("error_back_height").innerHTML = "";
        }
        //다리 길이 체크
        if (document.getElementById("id_leg_length").value == "") {
            document.getElementById("error_leg_length").innerHTML = "<strong>다리 길이를 입력해주세요.</strong>";
            isError = true;
        } else {
            document.getElementById("error_leg_length").innerHTML = "";
        }
        //좌석 깊이 체크
        if (document.getElementById("id_seat_depth").value == "") {
            document.getElementById("error_seat_depth").innerHTML = "<strong>좌석 깊이를 입력해주세요.</strong>";
            isError = true;
        } else {
            document.getElementById("error_seat_depth").innerHTML = "";
        }

        //정면 사진 체크
        if (document.getElementById("id_front_picture").files.length == 0) {
            document.getElementById("error_front_picture").innerHTML = "<strong>정면사진을 업로드해주세요.</strong>";
            isError = true;
        } else {
            document.getElementById("error_front_picture").innerHTML = "";
        }
        //측면 사진 체크
        if (document.getElementById("id_side_picture").files.length == 0) {
            document.getElementById("error_side_picture").innerHTML = "<strong>측면사진을 업로드해주세요.</strong>";
            isError = true;
        } else {
            document.getElementById("error_side_picture").innerHTML = "";
        }

        if ($('input:checkbox[id="id_check1"]').is(":checked") != true) {
            document.getElementById("error_check1").innerHTML = "<strong>동의를 해주셔야합니다.</strong>";
            alert('동의를 해주셔야합니다.');
            isError = true;
        } else {
            document.getElementById("error_check1").innerHTML = "";
        }
        if ($('input:checkbox[id="id_check2"]').is(":checked") != true) {
            document.getElementById("error_check2").innerHTML = "<strong>동의를 해주셔야합니다.</strong>";
            alert('동의를 해주셔야합니다.');
            isError = true;
        } else {
            document.getElementById("error_check2").innerHTML = "";
        }

        if (isError == true) {
            return;
        }

        document.getElementById("MyForm").submit();

    });

    $(document).ready(function () {

    });




});
