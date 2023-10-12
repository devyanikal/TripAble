import React from 'react';
import axios from 'axios';
import { useState,useEffect } from 'react';
import CardTemplate from './Card';
import { Grid } from '@mui/material';

function ViewPlaces(){
  const [value, setValue] = useState("");
  const [disablity, setDisability] = useState("");
    const [details, setDetails] = useState([],);
    const [isLoading, setLoading] = useState(true);
    let dict={wu: '',vi: '',si: '',hi: ''};
    useEffect(() =>{
        let data;
        console.log(disablity)
        if (disablity=="wu"){dict={wu: true,vi: '',si: '',hi: ''}}
        else if (disablity=="vi"){dict={wu: '',vi: true,si: '',hi: ''}}
        else if (disablity=="si"){dict={wu: '',vi: '',si: true,hi: ''}}
        else if (disablity=="hi"){dict={wu: '',vi: '',si: '',hi: true}}
        console.log(dict)
        let url='http://127.0.0.1:8000/explore?city='+value+'&wheelchair_user='+dict.wu+'&hearing_impaired='+dict.hi+'&visual_impaired='+dict.vi+'&speech_impaired='+dict.si
        console.log(url)
        axios.get(url)
            .then(res => {
                data=res.data;
                setDetails({
                    details: data
                });
                setLoading(false);
            })
            .catch(err => { })
    },[value,disablity]);

    if (isLoading) {
        return (
          <div>
          <h2>loading....</h2>
        </div>
        )
      } else {
    
        return (
            <div>
              
<Grid container spacing={2}>


<div className="destination-list">
{/* style={{marginLeft: 10 + 'em'}} */}

<div style={{marginLeft: 10 + 'em'}}>
          <h5>Choose city:</h5>
            <select id="places" value={value} onChange={(event)=>{setValue(event.target.value)}} class="form-select form-select-lg mb-3" aria-label=".form-select-lg example" >
              <option value="">ALL</option>
              <option value="Manali">Manali</option>
              <option value="Udaipur">Udaipur</option>
            </select>
            </div>  
            <div style={{marginLeft: 10 + 'em'}}>
              <h4>Choose Aids:</h4>
            <select onChange={(event)=>{setDisability(event.target.value)}}  id="colours">
            <option value="">ALL</option>
              <option value="wu">Wheelchair user</option>
              <option value="vi">Visually Imapired</option>
              <option value="hi">Hearing Imapired</option>
              <option value="si">Speech Imapired</option>
            </select>
        </div>

<Grid container item spacing={3}>
        {details.details.map((place, id) => (
            <div key={id}> {console.log(place.image)}
          
          <CardTemplate key={id} image={place.image} name={place.place_name} description={place.About}/>
          </div>
        ))}
        </Grid>
        
      </div>
      </Grid>
            </div>      
    )}

  }

export default ViewPlaces;