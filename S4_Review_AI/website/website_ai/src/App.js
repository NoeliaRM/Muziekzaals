import './App.css';
import axios from "./axios/axios"
import * as FileSaver from 'file-saver'
import * as XLSX from 'xlsx'


function App() {
// adds data to db
  const change_input = (e) => {
    let file = e.target.files[0]
    let reader = new FileReader()
    reader.readAsDataURL(file)
    reader.onload = function (e) {
        let rawLog = reader.result.split(',')[1]; //base64

        var body = {'data': JSON.stringify(rawLog) } //converts json to string
        axios.post('/review/data', body)
            .then(res => {
              alert("done!")
            }).catch(e => {
            alert('No server response')
      })
    }
  }

  // const download = async () =>
  // {
  //   var result = []
  //   await axios.get('/review/download')
  //     .then(res => {
  //       result = JSON.parse(res.data)
  //     })
  //     .catch(err => {
  //       alert='something went wrong'
  //     })
      
  //   var Sheets_value = {}
  //   var SheetNames_value = []
    
  //   Sheets_value['Results']= XLSX.utils.json_to_sheet(result)
  //   SheetNames_value.push("Results")
  //   const filename = "Results_" + new Date().toLocaleString()  + '_.xlsx'
  //   const wb = { Sheets: Sheets_value,
  //               SheetNames: SheetNames_value};

  //   const excelBuffer = XLSX.write(wb, { bookType: 'xlsx', type: 'array' });
  //   const data = new Blob([excelBuffer], {type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8'});
  //   FileSaver.saveAs(data, filename);
  // }

  const predict = async (e) =>{ 
    let file = e.target.files[0]
    let reader = new FileReader()
    reader.readAsDataURL(file)
    reader.onload = function (e) {
        let rawLog = reader.result.split(',')[1];

        var body = {'data': JSON.stringify(rawLog) }

        axios.post('/review/predict', body)
            .then(res => {
              var result = JSON.parse(res.data) //convert string to json
              var Sheets_value = {}
              var SheetNames_value = []
              
              Sheets_value['Results']= XLSX.utils.json_to_sheet(result) //change json to format acceptable by excel
              SheetNames_value.push("Results") //add sheetname 
              const filename = "Results_" + new Date().toLocaleString()  + '_.xlsx' //compose filename
              const wb = { Sheets: Sheets_value,
                          SheetNames: SheetNames_value}; // sotre object composed of sheet and sheetname

              const excelBuffer = XLSX.write(wb, { bookType: 'xlsx', type: 'array' }); //writes into excel format  the objects (that where an in array)
              const data = new Blob([excelBuffer], {type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8'}); // format compatible with xlsx
              FileSaver.saveAs(data, filename);
            }).catch(e => {
            alert('No server response')
      })
    }
  }

  return (
    <div className="App">
      <label htmlFor="csv-upload" className="csv-upload">Upload your CSV</label>
      <input id="csv-upload" type="file" accept=".csv" onChange={(e) => change_input(e)} />

      <br/>
      <br/>
      <br/>
      <br/>
      <br/>

       {/* <button onClick={() => download()}>Download csv</button>  */}

      <br/>
      <br/>
      <br/>
      <br/>
      <br/>

      <label htmlFor="predict" className="predict">Predict</label>
      <input id="predict" type="file" accept=".csv" onChange={(e) => predict(e)} />
    </div>
  );
}

export default App;
