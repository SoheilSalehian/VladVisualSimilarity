// *********************************************
// GENERATED FILE -- DO NOT EDIT PLEASE
// Parameterized with:
//
// EndpointName = index
// RequestName = dataPath
// RequestType = string
// ResponseName = status
// ResponseType = string
// *********************************************

package main

import (
	"encoding/json"
	"net/http"

   
  

	"github.com/go-kit/kit/endpoint"
	"golang.org/x/net/context"
)

// Request
type indexRequest struct {
  dataPath string `json:"dataPath"`
}

// Response
type indexResponse struct {
  status string `json:"status"`
	Err    string            `json:"err,omitempty"`
}

// Endpoint(s)
func makeindexEndpoint(svc indexService) endpoint.Endpoint {
	return func(ctx context.Context, request interface{}) (interface{}, error) {
  req := request.(indexRequest)
  serviceOutput, err := svc.Callindex(req.dataPath)
		if err != nil {
      return indexResponse{ serviceOutput, err.Error() }, nil
		}
    return indexResponse{ serviceOutput, "" }, nil
	}
}

// Decode Request
func decodeindexRequest(_ context.Context, r *http.Request) (interface{}, error) {
var request indexRequest
	if err := json.NewDecoder(r.Body).Decode(&request); err != nil {
		return nil, err
	}
	return request, nil
}

// Encode Response
func encodeResponse(_ context.Context, w http.ResponseWriter, response interface{}) error {
	return json.NewEncoder(w).Encode(response)
}

