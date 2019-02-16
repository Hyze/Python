import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 2.3
import QtQuick.Dialogs 1.2



ApplicationWindow {
    title: qsTr("Hello World")
    width: 640
    height: 680
    visible: true

    menuBar: MenuBar {
        Menu {
            title: qsTr("&File")

            MenuItem {
                text: qsTr("E&xit")
                onTriggered: Qt.quit();
            }
            MenuItem{
                text: qsTr("Open")
                onTriggered: textee.text = "Open clicked";
            }
        }
    }

    /*  Text{
        id:textee
        text: qsTr("Hello World")
        color: "red"
        font.pointSize: 20
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        }*/

    Frame {
        anchors.rightMargin: 0
        anchors.bottomMargin: 0
        anchors.leftMargin: 0
        anchors.topMargin: 5
        anchors.fill: parent

        Rectangle{
            id : monRectangle
            width: 200
            height: 300

            Image{
                id:image1
                anchors.fill: parent
                source: "img/img1.jpg"
            }

            Text{

                text: qsTr("Image 1")
                color: "white"
                font.pointSize: 20
                anchors.horizontalCenter: parent.horizontalCenter;
            }

            MouseArea{
                anchors.fill: parent
                hoverEnabled: true
                onEntered:
                {
                    monRectangle.opacity=0.5
                    //console.log("entered");
                }
                onExited:
                {
                    monRectangle.opacity=1
                    //console.log("exit");
                }
                Button{
                    id:bouton1
                    text: qsTr("Changer")
                    anchors.horizontalCenter: parent.horizontalCenter;
                    anchors.verticalCenter: parent.verticalCenter;
                    onClicked:
                    {
                        fileDialog1.open()
                        console.log("entered");

                    }
                }

            }

            FileDialog{
                id:fileDialog1
                title: "Choisissez un fichier"

                nameFilters: [ "Image files (*.png *.jpg)"]
                onAccepted: {
                    console.log("You chose: " + fileDialog1.fileUrls)

                    image1.source = fileUrl

                }
                onRejected: {
                    console.log("Canceled")
                    Qt.quit()
                }
                //Component.onCompleted: visible = true


            }
        }

        Rectangle{
            id : monRectangle2
            width: 200
            height: 300
            anchors.left: monRectangle.right
            anchors.leftMargin: 10;


            Image{
                id:image2
                anchors.fill: parent
                source: "img/img2.jpg"
            }

            Text{

                text: qsTr("Image 2")
                color: "white"
                font.pointSize: 20
                anchors.horizontalCenter: parent.horizontalCenter;
            }



            MouseArea{
                anchors.fill: parent
                hoverEnabled: true
                onEntered:
                {
                    monRectangle2.opacity=0.5
                    //console.log("entered");
                }
                onExited:
                {
                    monRectangle2.opacity=1
                    //console.log("exit");
                }
                Button{
                    id:bouton2
                    text: qsTr("Changer")
                    anchors.horizontalCenter: parent.horizontalCenter;
                    anchors.verticalCenter: parent.verticalCenter;
                    onClicked:
                    {
                        fileDialog.open()
                        console.log("entered");

                    }

                }

            }

            FileDialog{
                id:fileDialog
                title: "Choisissez un fichier"
                nameFilters: [ "Image files (*.png *.jpg)"]
                onAccepted: {
                    console.log("You chose: " + fileDialog.fileUrls)

                    image2.source = fileUrl

                }
                onRejected: {
                    console.log("Canceled")
                    Qt.quit()
                }
                //Component.onCompleted: visible = true


            }

        }


        Flickable{

            id:flickImg2
            anchors.top:monRectangle2.bottom
            anchors.topMargin:10
            width: 600
            height: 200
            contentWidth: img3.width
            contentHeight: img3.height
            clip:true
            Image{
                id:img3
                source:"img/img3.jpg"
                width:800
                height:800
            }
        }

    }







}

