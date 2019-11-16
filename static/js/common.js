//checkbox全选
 function setItemCheckBox(flag) {
    $(":checkbox[name=checkBtn]").prop("checked",flag);
  }
  $(function () {
    //点击全选
    $("#selectAll").click(function(){
      //1.获取全选的状态
      var flag = this.checked;//获取全选的状态
      if(flag){
        $(this).prop("checked", true);
      }else{
        $(this).prop("checked", false);
      }
      //var flag = $(":checkbox[name=selectAll]").attr("checked");//jquery-1.5.1的用法
      //2.让所有条目的复选框与全选的状态同步
      //alert(flag);
      setItemCheckBox(flag);
    });
    //给所有复选框添加事件
    $(":checkbox[name=checkBtn]").click(function(){
      var flagV = this.checked;
      if(flagV){
        $(this).prop("checked", true);
      }else{
        $(this).prop("checked", false);
      }
      //获取所有复选框的个数
      var len = $(":checkbox[name=checkBtn]").length;
      //获取所有被选中的复选框的个数
      var checked_len = $(":checkbox[name=checkBtn]:checked").length;
      if(len == checked_len){
        //alert("全选中了");
        $("#selectAll").prop("checked",true);
      } else if(checked_len == 0) {
        $("#selectAll").prop("checked",false);
      } else {
        $("#selectAll").prop("checked",false);
      }
    });
  });

 // //点击弹出指定输入框
 // function showMask(id) {
 //     var realId="#"+id;
 //     $(realId).show();
 // }
//弹出层点击关闭
$(function () {
    $("#closeMase").click(function () {
        $("#addMask").css("display","none");
        $("#editMask").css("display","none");
        $("#exportMask").css("display","none");
    });
});

function checkInput() {
    var inputList = $(this).siblings();
    console.log(inputList);
}